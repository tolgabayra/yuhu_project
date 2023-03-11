import React from 'react'
import { Outlet } from 'react-router-dom'
import Navbar from '../components/home/Navbar'

type Props = {}

export default function HomeLayout({ }: Props) {
    return (
        <div>
            <Navbar />

            <div className="container mx-auto">
                <div className="flex flex-row flex-wrap py-4">
                    <aside className="w-full sm:w-1/3 md:w-1/4 px-2">
                        <div className="sticky top-0 p-4 w-full">


                            <ul className="flex flex-col overflow-hidden font-serif">
                                <li className='bg-gray-300 mb-3 p-1 rounded-sm hover:bg-gray-400 hover:text-gray-100 duration-300 hover:cursor-pointer'>Home</li>
                                <li className='bg-gray-300 mb-3 p-1 rounded-sm hover:bg-gray-400 hover:text-gray-100 duration-300 hover:cursor-pointer'>Profile</li>
                                <li className='bg-gray-300 mb-3 p-1 rounded-sm hover:bg-gray-400 hover:text-gray-100 duration-300 hover:cursor-pointer'>Settings</li>
                                <li className=' bg-gray-300 p-1 rounded-sm hover:bg-gray-400 hover:text-gray-100 duration-300 hover:cursor-pointer'>Log out</li>

                            </ul>
                        </div>
                    </aside>
                    <main role="main" className="w-full sm:w-2/3 md:w-3/4 pt-1 px-24">

                    <Outlet />

                    </main>
                </div>
            </div>
            <footer className="mt-auto">
                ...
            </footer>



        </div>
    )
}