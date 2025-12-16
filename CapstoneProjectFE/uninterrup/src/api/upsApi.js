import axiosClient from "./axiosClient";

export const getUPSUnits = async () => {
  try {
    const res = await axiosClient.get("/api/");
    console.log(res.data); // <- check the structure
    return res.data;
  } catch (error) {
    console.error("Error fetching UPS units:", error);
    return [];
  }
 }; 