import { createSlice } from "@reduxjs/toolkit";

const dataSlice = createSlice({
  name: "data",

  initialState: {
    messages: [],
    loading: false,
    model: "",
  },

  reducers: {
    pushMessage: (state, action) => {
      state.messages = [action.payload, ...state.messages];
    },
    setloading: (state, action) => {
      state.loading = action.payload;
    },
    setModel: (state, action) => {
      state.model = action.payload;
    },
  },
});
export const getMessages = (state) => state.data.messages;
export const getLoading = (state) => state.data.loading;
export const getModel = (state) => state.data.model;

export const { pushMessage, setloading, setModel } = dataSlice.actions;
export default dataSlice.reducer;
