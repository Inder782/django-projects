"use client";
import React from "react";

const page = () => {
  const fetchSecureData = async () => {
    const token = localStorage.getItem("access_token"); // Retrieve JWT token

    if (!token) {
      console.error("No token found, user not authenticated.");
      return;
    }

    const response = await fetch("http://127.0.0.1:8000/secure", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`, // Include JWT token
        "Content-Type": "application/json",
      },
    });

    const data = await response.json();

    if (response.ok) {
      console.log("Secure data:", data);
    } else {
      console.error("Failed to fetch secure data:", data);
    }
  };
  fetchSecureData();
  return <div>This is for sendig to the secure page</div>;
};

export default page;
