import React from 'react'
import Link from 'next/link'

const Navbar = () => {
  return (
    <nav className="bg-blue-600 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-xl font-bold">
          <Link href="/">MyApp</Link>
        </div>
        <ul className="flex space-x-4">
          <li>
            <Link href="/" className="hover:text-blue-200">Home</Link>
          </li>
          <li>
            <Link href="/signin" className="hover:text-blue-200">Sign In</Link>
          </li>
          <li>
            <Link href="/todos" className="hover:text-blue-200">Todos</Link>
          </li>
        </ul>
      </div>
    </nav>
  )
}

export default Navbar