import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";


const authSlice = createSlice({
    name: "auth",
    initialState: {
        user: localStorage.getItem("user_id") ?? false
    },

    reducers: {
        login: (state) => {
            state.user = true
        },
        logout: (state) => {
            state.user = false
        }
    }
})


export const { login, logout } = authSlice.actions
export default authSlice.reducer