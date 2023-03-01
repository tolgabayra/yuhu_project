import React from 'react'

type Props = {}

export default function index({ }: Props) {
  return (
    <div>
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
      </nav>


      <div className="container mx-auto my-10 sm:px-20  flex justify-center">

        <div className=" rounded overflow-hidden border w-full lg:w-6/12 md:w-6/12 bg-white mx-3 md:mx-0 lg:mx-0">
          <div className="w-full flex justify-between p-3">
            <div className="flex">
              <div className="rounded-full h-8 w-8 bg-gray-500 flex items-center justify-center overflow-hidden">
                <img src="https://avatars0.githubusercontent.com/u/38799309?v=4" alt="profilepic" />
              </div>
              <span className="pt-1 ml-2 font-bold text-sm">braydoncoyer</span>
            </div>
            <span className="px-2 hover:bg-gray-300 cursor-pointer rounded"><i className="fas fa-ellipsis-h pt-2 text-lg"></i></span>
          </div>
          <img className="w-full bg-cover" src="https://3.bp.blogspot.com/-Chu20FDi9Ek/WoOD-ehQ29I/AAAAAAAAK7U/mc4CAiTYOY8VzOFzBKdR52aLRiyjqu0MwCLcBGAs/s1600/DSC04596%2B%25282%2529.JPG" />
          <div className="px-3 pb-2">
            <div className="pt-2">
              <i className="far fa-heart cursor-pointer"></i>
              <span className="text-sm text-gray-400 font-medium">12 likes</span>
            </div>
            <div className="pt-1">
              <div className="mb-2 text-sm">
                <span className="font-medium mr-2">braydoncoyer</span> Lord of the Rings is my favorite film-series. One day I'll make my way to New Zealand to visit the Hobbiton set!
              </div>
            </div>
            <div className="text-sm mb-2 text-gray-400 cursor-pointer font-medium">View all 14 comments</div>
            <div className="mb-2">
              <div className="mb-2 text-sm">
                <span className="font-medium mr-2">razzle_dazzle</span> Dude! How cool! I went to New Zealand last summer and had a blast taking the tour! So much to see! Make sure you bring a good camera when you go!
              </div>
            </div>
          </div>
        </div>





        <div className="social-icons">
          <a className="social-icon social-icon--codepen" href="https://codepen.io/braydoncoyer" target="_blank">
            <i className="fa fa-codepen"></i>
            <div className="tooltip">Codepen</div>
          </a>
          <a className="social-icon social-icon--twitter" href="https://twitter.com/BraydonCoyer" target="_blank">
            <i className="fa fa-twitter"></i>
            <div className="tooltip">Twitter</div>
          </a>
        </div>

      </div>
    </div>
  )
}