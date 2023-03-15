import { Avatar, Box, Button, Card, CardBody, CardFooter, CardHeader, Flex, Heading, IconButton, Image, Text, useToast } from '@chakra-ui/react'
import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  useDisclosure,
  Input,
  InputGroup,
  InputLeftElement,
  FormControl,
  FormLabel,
  Textarea

} from '@chakra-ui/react'
import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { BiLike, BiChat, BiShare, BiCommentAdd } from "react-icons/bi"
import Navbar from '../components/home/Navbar'
import { appAxios } from '../utils/appAxios'


export default function Home() {

  const toast = useToast()


  const [file, setFile] = useState();
  const [content, setContent] = useState();

  const submitCreatePostRequest = () => {

    let bodyFormData = new FormData()
    bodyFormData.append("content", content)
    bodyFormData.append("user_id", localStorage.getItem("user_id"))
    bodyFormData.append("media", file)

    axios({
      method: "post",
      url: "http://localhost:5000/api/v1/posts",
      data: bodyFormData,
      headers: { "Content-Type": "multipart/form-data" }
    })
      .then((res) => {
        console.log(res);
        onPostClose()
        toast({
          title: 'Post created.',
          description: "We've created your post for you.",
          status: 'success',
          position: "top-right",
          duration: 1000,
          isClosable: true,
        })
      })
      .catch(err => {
        console.log(err);
        toast({
          title: 'Upss, Sorry ',
          description: "Post can not created.",
          status: 'warning',
          position: "top-right",
          duration: 1000,
          isClosable: true,
        })
      })

  }



  const [isLike, setIsLike] = useState(false)
  const [comments, setComments] = useState([
    { author: "John Doe", content: "Great post!" },
    { author: "Jane Doe", content: "Thanks for sharing!" }
  ]);


  const handleLikeClick = () => {
    setIsLike(!isLike)
  }

  const { isOpen: isCommentOpen, onOpen: onCommentOpen, onClose: onCommentClose } = useDisclosure()
  const { isOpen: isPostOpen, onOpen: onPostOpen, onClose: onPostClose } = useDisclosure()
  const commentCount = comments.length


  const [posts, setPosts] = useState<Array<any>>([])




  useEffect(() => {
    appAxios.get("/api/v1/posts")
      .then((res) => {
        console.log(res.data.posts);
        setPosts(res.data.posts)
      })
      .catch(err => {
        console.log(err);

      })
  }, [])


  return (
    <div>

      {/*  Comment Modal */}
      <Modal isOpen={isCommentOpen} onClose={onCommentClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Comments ({commentCount})</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <Box mb={4}>
              <InputGroup size="md">
                <InputLeftElement
                  pointerEvents="none"
                  children={<BiCommentAdd color="gray.300" />}
                />
                <Input placeholder="Yorumunuzu yazın" />
              </InputGroup>
            </Box>
            {comments.map((comment, index) => (
              <Box key={index} p="4">
                <Text fontSize="lg" fontWeight="bold">{comment.author}</Text>
                <Text>{comment.content}</Text>
              </Box>
            ))}
          </ModalBody>

          <ModalFooter>
            <Button colorScheme='blue' mr={3} onClick={onCommentClose}>
              Close
            </Button>
            <Button variant='ghost' onClick={() => {
              const newComment = {
                author: "John Doe",
                content: "Lorem ipsum dolor sit amet"
              };
              setComments([...comments, newComment]);
            }}>Comment</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>


      {/* Post Modal */}
      <Modal isOpen={isPostOpen} onClose={onPostClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>New Post</ModalHeader>
          <ModalCloseButton />
          <ModalBody>


            <form className=' border-solid  p-3'>
              <FormControl id="post-body" isRequired>
                <FormLabel>Content</FormLabel>
                <Textarea onChange={(e) => setContent(e.target.value)} />
                <FormControl id="image-upload" isRequired>
                  <div className="App">
                    <h2>Add Image:</h2>
                    <input type="file" onChange={(e) => {
                      console.log(e.target.files[0]);
                      setFile(e.target.files[0]);
                    }} />
                    <img src={file} />

                  </div>
                </FormControl>
              </FormControl>
            </form>
          </ModalBody>

          <ModalFooter>
            <Button colorScheme='blue' mr={3} onClick={onPostClose}>
              Close
            </Button>
            <Button onClick={submitCreatePostRequest} variant='' bgColor="green.500" textColor="white">Create</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>


      <Card bg="gray.300" maxW="md" mb="10">
        <CardBody>
          <Flex flex='1' gap='4' alignItems='center' flexWrap='wrap'>
            <Avatar name='Segun Adebayo' src='https://bit.ly/sage-adebayo' />
            <Box>
              <Input onClick={onPostOpen} width="80" placeholder='Create Post' />
            </Box>
          </Flex>
        </CardBody>
      </Card>



      <hr />

      {
        posts.map((post, index) => {
          return (

            <Card key={index} maxW='md' backgroundColor="gray.100">
              <CardHeader>
                <Flex>
                  <Flex flex='1' gap='4' alignItems='center' flexWrap='wrap'>
                    <Avatar name={post.username} src={``} />

                    <Box>
                      <Heading size='sm'>{post.username}</Heading>
                      <Text>{post.email}</Text>
                    </Box>
                  </Flex>
                  <IconButton
                    variant='ghost'
                    colorScheme='gray'
                    aria-label='See menu'
                  />
                </Flex>
              </CardHeader>
              <CardBody>
                <Text>
                  {post.content}
                  {post.media}
                </Text>
              </CardBody>
              <Image
                objectFit='cover'
                src={'http://localhost:5000' + post.media}
                alt='Chakra UI'
              />

              <CardFooter
                justify='space-between'
                flexWrap='wrap'
                sx={{
                  '& > button': {
                    minW: '136px',
                  },
                }}
              >
                <Button colorScheme={isLike ? "red" : "gray"} transition="all 0.2s" _active={{ bg: isLike ? "red.600" : "gray.300" }} onClick={handleLikeClick} flex='1' variant='ghost' leftIcon={<BiLike />}>
                  Like
                </Button>
                <Button onClick={onCommentOpen} flex='1' variant='ghost' leftIcon={<BiChat />}>
                  Comment ({commentCount})
                </Button>
                <Button flex='1' variant='ghost' leftIcon={<BiShare />}>
                  Share
                </Button>
              </CardFooter>
            </Card>


          )
        })
      }



    </div>
  )
}




