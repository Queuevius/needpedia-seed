import React from "react";
import { useSelector } from "react-redux";
import { getLoading } from "../slices/dataSlice";

const useGetLoading = () => {
  const loading = useSelector(getLoading);
  return loading;
};

export default useGetLoading;
