import { createSlice } from "@reduxjs/toolkit";

const authSlice = createSlice({
    name: 'auth',
    initialState: {
        isAuthenticated: false,
    },
    reducers: {
        setLogin: (state) => {
            state.isAuthenticated = true;
        },
        setLogout: (state) => {
            state.isAuthenticated = false;
        },
    },
});

export const {setLogin, setLogout} = authSlice.actions;
export default authSlice.reducer;