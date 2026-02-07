SET UP TS Project

npm init -y
npm i typescript
npx tsc --init
change tsconfig.json
"rootDir": "./src",
    "outDir": "./dist",
Run project ko 
packager.json
"scripts:{
    "dev": "tsc -b && node dist/index.js"
}
and then run 
npm run dev


npm i pg @types/pg
pg->libary
@types/pg-> give we tyeps
