import pg from 'pg';
import dotenv from 'dotenv';
import express from 'express';
dotenv.config();
const pgclient = new pg.Client({ connectionString: process.env.DATABASE_URL });
const app = express();
app.use(express.json());
const db = async () => {
    pgclient.connect()
        .then(() => console.log('Connected to PostgreSQL database'))
        .catch((err) => console.error('Error connecting to PostgreSQL database:', err));
};
db();
app.get('/', (req, res) => {
    res.send('Hello, World!');
});
// CREATE TABLE users (
//     id SERIAL PRIMARY KEY,
//     username VARCHAR(50) UNIQUE NOT NULL,
//     email VARCHAR(255) UNIQUE NOT NULL,
//     password VARCHAR(255) NOT NULL,
//     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP 
// );
// sql injection example
app.post('/addusers', async (req, res) => {
    const { username, email, password } = req.body;
    try {
        const insertQuery = `INSERT INTO users (username,email,password) VALUES ('${username}', '${email}', '${password}')`; // here sql injection happens if user send ab noramla data like 
        console.log(insertQuery);
        // noraml query example : INSERT INTO users (username,email,password) VALUES ('cy1wber', 'cyber1@wgmail.com', '123456')
        // sql injection example : INSERT INTO users (username,email,password) VALUES ('cy1wber', 'cyber1@wgmail.com', ''); DELETE * FROM users')
        // this happend user password field me   "password": "'); DELETE * FROM users" or query agar db chali to db 
        // user table ke sare data delete ho jayega hae hota sql injection attack user pan wo kuch bhi send kar sakta hae 
        //   const response = await pgclient.query(insertQuery) 
        const inserQuerynotsqlInjection = 'INSERT INTO users (username,email,password) VALUES ($1, $2, $3)'; // this is parameterized query and it is safe from sql injection attack
        console.log(inserQuerynotsqlInjection);
        const response = await pgclient.query(inserQuerynotsqlInjection, [username, email, password]); // this is parameterized query and it is safe from sql injection attack
        // ese kya inserQuerynotsqlInjection as reach to dabase then and value matlab postsql dabase ek query and value and done alga alg hote hae first me query ke ssate value jara hi thi ab value and query alga alg hote hae to sql injection attack nhi hota hae
        // ese query and value alga alg hote hae to sql injection attack nhi hota hae kyuki user input value ke sath query nahi jura hota hae to user input me kuch bhi send kar sakta hae but wo query ke sath nahi jura hota hae to sql injection attack nhi hota hae
        res.send('User added successfully');
    }
    catch (err) {
        console.error('Error adding user:', err);
        res.send('Error adding user');
    }
});
// Foregin key mean agar user 3 hae and address table me user_id 3 ke sath address add karna hae to user_id 3 hona chahiye user table me agar user_id 3 nahi hoga to address table me user_id 3 ke sath address add nahi hoga kyuki foreign key constraint hota hae
// like forgein key let connected to two table like users and address (multiple address)
// CREATE TABLE users (
//     id SERIAL PRIMARY KEY,
//     username VARCHAR(50) UNIQUE NOT NULL,
//     email VARCHAR(255) UNIQUE NOT NULL,
//     password VARCHAR(255) NOT NULL,
//     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP 
// );
// when we create adress table  user_id is foreign key 
// CREATE TABLE addresses (
//     id SERIAL PRIMARY KEY,
//     user_id INTEGER NOT NULL,
//     city VARCHAR(100) NOT NULL,
//     country VARCHAR(100) NOT NULL,
//     street VARCHAR(255) NOT NULL,
//     pincode VARCHAR(20),
//     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
//     FOREIGN KEY ("user_id") REFERENCES users(id) ON DELETE CASCADE
// );
// ye liek imp ki key hae nad useka refere users table ke id on DELETE CASCADE agar aapko user ko delete karna hoga to panle use adres ko deleter karna use baad app user delete kar skato hae 
// casecade me ek baar ek baar girna 
// This is called a relationship , which means that the Address table is related to the Users table.
// When defining the table, you need to define the relationship 
// one to many relationship means one user can have multiple addresses but one address can belong to only one user
// relation table example 
app.post('/relation', async (req, res) => {
    const { username, email, password, city, country, street, pincode } = req.body;
    try {
        const queryUser = 'INSERT INTO users (username,email,password) VALUES ($1, $2, $3) RETURNING id'; // RETURNING id is used to get the id of the user that we just inserted into the database 
        const queryAddress = 'INSERT INTO addresses (user_id, city, country, street, pincode) VALUES ($1, $2, $3, $4, $5)';
        const responseUser = await pgclient.query(queryUser, [username, email, password]); // this is parameterized query and it is safe from sql injection attack
        const userId = responseUser.rows[0].id; // get the id of the user that we just inserted into the database 
        console.log(userId);
        const responseAddress = await pgclient.query(queryAddress, [userId, city, country, street, pincode]); // this is parameterized query and it is safe from sql injection attack
        res.send('User and address added successfully');
    }
    catch (err) {
        console.error('Error adding user and address:', err);
        res.send('Error adding user and address');
    }
});
function blockFor(ms) {
    const end = Date.now() + ms;
    while (Date.now() < end) {
        // busy wait – blocks event loop
        console.log('Blocking for', ms, 'milliseconds');
    }
}
// transaction example
// Good question to have at this point is what queries are run when the user signs up and sends both their information and their address in a single request.
// Do we send two SQL queries into the database? What if one of the queries (address query for example) fails? 
// This would require transactions  in SQL to ensure either both the user information and address goes in, or neither does
// transaction se kya jab dono query run nahi hote tab tak database me changes nahi hote hae 
// agar query chali and send me koi error aaya to transaction rollback ho jayega aur database me changes nahi hoga
app.post('/transaction', async (req, res) => {
    const { username, email, password, city, country, street, pincode } = req.body;
    try {
        const queryUser = 'INSERT INTO users (username,email,password) VALUES ($1, $2, $3) RETURNING id'; // RETURNING id is used to get the id of the user that we just inserted into the database 
        const queryAddress = 'INSERT INTO addresses (user_id, city, country, street, pincode) VALUES ($1, $2, $3, $4, $5)';
        await pgclient.query('BEGIN'); // start the transaction
        const responseUser = await pgclient.query(queryUser, [username, email, password]);
        const userId = responseUser.rows[0].id;
        console.log(userId);
        // blockFor(60 * 1000);
        const responseAddress = await pgclient.query(queryAddress, [userId, city, country, street, pincode]);
        await pgclient.query('COMMIT'); // commit the transaction
        res.send('User and address added successfully');
    }
    catch (err) {
        console.error('Error adding user and address:', err);
        res.send('Error adding user and address');
    }
});
app.get('/metadata', async (req, res) => {
    const id = req.query.id;
    try {
        const query = `SELECT username , email, id FROM users WHERE id = $1`;
        const response = await pgclient.query(query, [id]);
        const queryAddress = `SELECT * FROM addresses WHERE user_id = $1`;
        const responseAddress = await pgclient.query(queryAddress, [id]);
        // here the probleme 2 alag alag db call ho rahae hae not sencse to 2 call in db 
        res.json({
            user: response.rows[0],
            address: responseAddress.rows // hame 0 nahi laga sakte agar to srif ek address show hame chaye sare address show karna hae to responseAddress.rows lagana hoga kyuki responseAddress.rows me sare address hote hae jo user ke sath connected hote hae
        });
    }
    catch (err) {
        console.error('Error fetching metadata:', err);
        res.send('Error fetching metadata');
    }
});
// join example
app.get('/join', async (req, res) => {
    const id = req.query.id;
    try {
        const query = `SELECT users.username, users.email, addresses.city, addresses.country, addresses.street, addresses.pincode FROM users JOIN addresses ON users.id = addresses.user_id WHERE users.id = $1`;
        const response = await pgclient.query(query, [id]);
        res.json(response.rows);
    }
    catch (err) {
        console.error('Error fetching metadata:', err);
        res.send('Error fetching metadata');
    }
});
// aggregate function example
app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
//# sourceMappingURL=index.js.map