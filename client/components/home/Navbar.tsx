import React from 'react'

type Props = {}

export default function Navbar({ }: Props) {
    return (
        <nav className="flex items-center justify-around flex-wrap bg-white p-6 shadow-md">
            <div className="flex items-center flex-shrink-0 text-gray-800 mr-6 cursor-pointer">
                <img src="https://i.ibb.co/KySZGdq/nt-ui-angular-src-assets-Logo-Pixelgram.png" alt="" />
            </div>
            <div className="text-sm w-64 mr-32">
                <input className="bg-gray-100 focus:outline-none focus:shadow-outline border border-gray-400 rounded py-1 px-4 block w-full appearance-none leading-normal" type="text" placeholder="Search" />
            </div>
            <div>
                <i className="far fa-user text-lg cursor-pointer"></i>
            </div>
        </nav>)
}