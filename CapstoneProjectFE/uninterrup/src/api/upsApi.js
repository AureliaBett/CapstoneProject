import axiosClient from "./axiosClient";

export const getUPSUnits = async () => {
  const res = await axiosClient.get("/ups/");
  return res.data;
};
