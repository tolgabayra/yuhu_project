import React from 'react'

type Props = {}

export default function Profile({ }: Props) {
    return (
        <div>

            <div className="max-w-4xl flex h-auto flex-wrap mx-auto my-32 lg:my-0">

                <div id="profile" className="w-full lg:w-3/5 rounded-lg lg:rounded-l-lg lg:rounded-r-none shadow-2xl bg-white opacity-75 mx-6 lg:mx-0">
                    <div className="p-4 md:p-12 text-center lg:text-left">
                        <div className="block lg:hidden rounded-full shadow-xl mx-auto -mt-16 h-48 w-48 bg-cover bg-center" style={{ backgroundImage: `url(${"https://randomuser.me/api/portraits/lego/0.jpg"})` }}></div>

                        <h1 className="text-3xl font-bold pt-8 lg:pt-0">Mr Block Heads</h1>
                        <div className="mx-auto lg:mx-0 w-4/5 pt-3 border-b-2 border-teal-500 opacity-25"></div>
                        <p className="pt-4 text-base font-bold flex items-center justify-center lg:justify-start"><img className="mr-3" src="https://img.icons8.com/dusk/30/000000/new-job.png" />Website Builder</p>
                        <p className="pt-2 text-gray-600 text-xs lg:text-sm flex items-center justify-center lg:justify-start"><img className="mr-3" src="https://img.icons8.com/officel/30/000000/worldwide-location.png" />Location:<a href="https://what3words.com/after.takes.shorts" target="_blank"> ///after.takes.shorts</a></p>
                        <p className="pt-8 text-sm">Inspire and Develop the Builders of Tomorrow</p>
l
                        <div className="pt-12 pb-8">
                            <button className="bg-teal-700 hover:bg-blue-800 hover:text-white text-black font-bold py-2 px-4 rounded-full">
                                Get In Touch
                            </button>
                        </div>

                        <div className="mt-6 pb-16 lg:pb-0 w-4/5 lg:w-full mx-auto flex flex-wrap items-center justify-between">
                            <a className="link opacity-100 hover:opacity-50" href="#" target="_blank"><img src="https://img.icons8.com/color/30/000000/linkedin-circled.png" /></a>
                            <a className="link opacity-100 hover:opacity-50" href="#" target="_blank"><img src="https://img.icons8.com/color/30/000000/facebook-circled.png" /></a>
                            <a className="link opacity-100 hover:opacity-50" href="#" target="_blank"><img src="https://img.icons8.com/color/30/000000/twitter-circled.png" /></a>
                            <a className="link opacity-100 hover:opacity-50" href="#" target="_blank"><img src="https://img.icons8.com/cute-clipart/30/000000/instagram-new.png" /></a>
                            <a className="link opacity-100 hover:opacity-50" href="#" target="_blank"><img src="https://img.icons8.com/color/30/000000/youtube-play.png" /></a>
                            <a className="link opacity-100 hover:opacity-50" href="#" target="_blank"><img src="https://img.icons8.com/color/30/000000/gitlab.png" /></a>
                            <a className="link opacity-100 hover:opacity-50" href="#" target="_blank"><img src="https://img.icons8.com/ios-filled/30/000000/github.png" /></a>
                        </div>

                    </div>

                </div>

                <div className="w-full lg:w-2/5">
                    <img src="https://randomuser.me/api/portraits/lego/0.jpg" className="rounded-none lg:rounded-lg shadow-2xl hidden lg:block" />

                </div>


            </div>


        </div>
    )
}