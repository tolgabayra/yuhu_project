import { Avatar, Box, Button, Card, CardBody, CardFooter, CardHeader, Flex, Heading, IconButton, Image, Text } from '@chakra-ui/react'
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
  InputLeftElement

} from '@chakra-ui/react'
import React, { useState } from 'react'
import { BiLike, BiChat, BiShare, BiCommentAdd } from "react-icons/bi"
import Navbar from '../components/home/Navbar'





export default function Home() {
  const [isLike, setIsLike] = useState(false)
  const [comments, setComments] = useState([
    { author: "John Doe", content: "Great post!" },
    { author: "Jane Doe", content: "Thanks for sharing!" }
  ]);
  const [posts, setPosts] = useState([
    {
      author: "John Doe",
      content: "Lorem ipsum dolor sit amet",
      image: "https://images.unsplash.com/photo-1531403009284-440f080d1e12?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80",
      comments: [
        { author: "Jane Doe", content: "Great post!" },
        { author: "John Smith", content: "Thanks for sharing!" }
      ]
    },
  ])
  const handleLikeClick = () => {
    setIsLike(!isLike)
  }


  const { isOpen, onOpen, onClose } = useDisclosure()


  const commentCount = comments.length



  return (
    <div>

      <Modal isOpen={isOpen} onClose={onClose}>
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
            <Button colorScheme='blue' mr={3} onClick={onClose}>
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




      <Card maxW='md' backgroundColor="gray.100">
        <CardHeader>
          <Flex>
            <Flex flex='1' gap='4' alignItems='center' flexWrap='wrap'>
              <Avatar name='Segun Adebayo' src='https://bit.ly/sage-adebayo' />

              <Box>
                <Heading size='sm'>Segun Adebayo</Heading>
                <Text>Creator, Chakra UI</Text>
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
            With Chakra UI, I wanted to sync the speed of development with the speed
            of design. I wanted the developer to be just as excited as the designer to
            create a screen.
          </Text>
        </CardBody>
        <Image
          objectFit='cover'
          src='https://images.unsplash.com/photo-1531403009284-440f080d1e12?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80'
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
          <Button onClick={onOpen} flex='1' variant='ghost' leftIcon={<BiChat />}>
            Comment ({commentCount})
          </Button>
          <Button flex='1' variant='ghost' leftIcon={<BiShare />}>
            Share
          </Button>
        </CardFooter>
      </Card>




    </div>
  )
}




