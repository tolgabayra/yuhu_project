import { useRoutes } from "react-router-dom";
import HomeLayout from "./layouts/HomeLayout";
import Home from "./pages/Home";
import Login from "./pages/Login";
import NotFoundPage from "./pages/NotFoundPage";
import Register from "./pages/Register";

export default function Router(){
    return useRoutes([
        {
            path: "home",
            element: <HomeLayout />,
            children: [
                {path: "", element: <Home />}
            ]
        },
        {
            path: "login",
            element: <Login />
            
        },
        {
            path: "register",
            element: <Register />
        },
        {
            path: "*",
            element: <NotFoundPage />
        }
    ])
}