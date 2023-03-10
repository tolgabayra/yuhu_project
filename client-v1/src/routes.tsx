import { useRoutes } from "react-router-dom";
import Login from "./pages/Login";
import NotFoundPage from "./pages/NotFoundPage";
import Register from "./pages/Register";

export default function Router(){
    return useRoutes([
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