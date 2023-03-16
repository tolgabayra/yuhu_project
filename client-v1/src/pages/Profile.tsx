import React, { useEffect, useState } from 'react'
import { appAxios } from '../utils/appAxios'

type Props = {}

export default function Profile({ }: Props) {
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [username, setUsername] = useState("")
    const [email, setEmail] = useState("")
    const [bio, setBio] = useState("")
    const [profileImage, setProfileImage] = useState("")

    const [userInfo, setUserInfo] = useState<any>({})


    useEffect(() => {
        appAxios.get(`api/v1/auth/me/${localStorage.getItem("user_id")}`)
        .then((res) => {
          console.log(res.data);
          setUserInfo(res.data)
        })
        .catch(err=>{
          console.log(err);
        })
    },[])




    return (
        <div>

            <div className="max-w-4xl flex h-auto flex-wrap mx-auto my-32 lg:my-0">

                <div id="profile" className="w-full lg:w-3/5 rounded-lg lg:rounded-l-lg lg:rounded-r-none  bg-white opacity-75 mx-6 lg:mx-0">
                    <div className="p-4 md:p-12 text-center lg:text-left">
                        <div className="block lg:hidden rounded-full  mx-auto -mt-16 h-48 w-48 bg-cover bg-center" style={{ backgroundImage: `url(${"https://randomuser.me/api/portraits/lego/0.jpg"})` }}></div>


                        <p className="pt-4 text-base flex items-center justify-center lg:justify-start"><img className="mr-3" src="https://img.icons8.com/dusk/30/000000/new-job.png" /> <span className='font-bold mr-2'>FirstName:</span>{userInfo.firstName}</p>
                        <p className="pt-4 text-base  flex items-center justify-center lg:justify-start"><img className="mr-3" src="https://img.icons8.com/dusk/30/000000/new-job.png" /> <span className='font-bold mr-2'>LastName:</span>{userInfo.lastName}</p>
                        <p className="pt-4 text-base  flex items-center justify-center lg:justify-start"><img className="mr-3" src="https://img.icons8.com/dusk/30/000000/new-job.png" /> <span className='font-bold mr-2'>Username:</span>{userInfo.username}</p>
                        <p className="pt-2  text-xs lg:text-sm flex items-center justify-center lg:justify-start"><img className="mr-3" src="https://img.icons8.com/officel/30/000000/worldwide-location.png" /> <span className='font-bold mr-2'>Email: </span> {userInfo.email}</p>
                        <p className="pt-8 text-sm"><span className=' font-bold'>Bio:</span> {userInfo.bio ?? "Write your own bio..."}</p>
                        
                    </div>

                </div>

                <div className="w-full lg:w-2/5">
                    <img src="https://randomuser.me/api/portraits/lego/0.jpg" className="rounded-none lg:rounded-lg hidden lg:block" />

                </div>


            </div>


        </div>
    )
}