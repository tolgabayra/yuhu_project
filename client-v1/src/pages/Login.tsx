import { Button, Input, InputGroup, InputRightElement, useToast } from '@chakra-ui/react'
import React, { useState } from 'react'
import { appAxios } from '../utils/appAxios'
type Props = {}

export default function Login({ }: Props) {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const [show, setShow] = useState(false)
  const handleClick = () => setShow(!show)

  const toast = useToast()




  const handleLogin = () => {
    appAxios.post("/api/v1/auth/login", {
      email,
      password
    })
      .then((res) => {
        toast({
          title: 'Login is successfully.',
          description: "We can redirect you to home",
          status: 'success',
          position: "top-right",
          duration: 1000,
          isClosable: true,
        })
      })
      .catch(err => {
        console.log(err);
        toast({
          title: 'Sorrry, Login is not successfully.',
          description: "Check your information or ethernet connection",
          status: 'warning',
          position: "top-right",
          duration: 1000,
          isClosable: true,
        })

      })
  }



  return (
    <div>
      <div className="min-h-screen flex justify-center items-center bg-white">
        <div className="p-10 border-[1px] -mt-10 border-slate-200 rounded-md flex flex-col items-center space-y-3">
          <div className="py-8">
            <img width="30" className="-mt-10" src="https://www.paypalobjects.com/images/shared/momgram@2x.png" />
          </div>
          <Input onChange={(e) => setEmail(e.target.value)} size="lg" borderColor="blue.500" placeholder='Email' />
          <div className="flex flex-col space-y-1">
            <InputGroup size='lg'>
              <Input
                borderColor="blue.500"
                pr='4.5rem'
                onChange={(e) => setPassword(e.target.value)}
                type={show ? 'text' : 'password'}
                placeholder='Enter password'
              />
              <InputRightElement width='4.5rem'>
                <Button h='1.75rem' size='sm' onClick={handleClick}>
                  {show ? 'Hide' : 'Show'}
                </Button>
              </InputRightElement>
            </InputGroup>
            <a className='font-bold text-[#0070ba]' href="/reset_password">Forgot Password</a>
          </div>
          <div className="flex flex-col space-y-5 w-full">
            <Button onClick={handleLogin} colorScheme='blue'>Log In</Button>
            <div className="flex items-center justify-center border-t-[1px] border-t-slate-300 w-full relative">
              <div className="-mt-1 font-bod bg-white px-5 absolute">Or</div>
            </div>
            <a className='bg-blue-500 p-2 text-white rounded-lg text-center font-bold' href="/register">Register</a>
          </div>
          <div className="flex space-x-1 p-20 text-sm">
            <p className="hover:underline cursor-pointer">German</p>
            <div className="border-r-[1px] border-r-slate-300"></div>
            <p className="font-bold hover:underline cursor-pointer">English</p>
          </div>
        </div>

        <div className="absolute bottom-0 w-full p-3 bg-[#F7F9FA] flex justify-center items-center space-x-3 text-[14px] font-medium text-[#666]">
          <a href="https://www.paypal.com/us/smarthelp/contact-us" target="_blank" className="hover:underline underline-offset-1 cursor-pointer">Contact Us</a>
          <a href="https://www.paypal.com/de/webapps/mpp/ua/privacy-full" target="_blank" className="hover:underline underline-offset-1 cursor-pointer">Privacy</a>
          <a href="https://www.paypal.com/de/webapps/mpp/ua/legalhub-full" target="_blank" className="hover:underline underline-offset-1 cursor-pointer">Legal</a>
          <a href="https://www.paypal.com/de/webapps/mpp/ua/upcoming-policies-full" target="_blank" className="hover:underline underline-offset-1 cursor-pointer">Policy </a>
          <a href="https://www.paypal.com/de/webapps/mpp/country-worldwide" target="_blank" className="hover:underline underline-offset-1 cursor-pointer">Worldwide </a>
        </div>
      </div>
    </div>
  )
}