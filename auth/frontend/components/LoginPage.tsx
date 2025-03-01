"use client";

import React from "react";
import { CreateUser } from "@/utils/CreateUser";

const LoginPage = () => {

  const handlesubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const data = new FormData(e.currentTarget);
    const username = data.get("username");
    const password = data.get("password");

  
    if (username && password){
      CreateUser(username,password)
    }
    
  };
  return (
    <form className="flex gap-10" onSubmit={handlesubmit}>
      <label>Enter username here</label>
      <input
        type="text"
        name="username"
        placeholder="username"
        className="bg-grey-500"
      />
      <input
        type="password"
        name="password"
        placeholder="password"
        className="bg-grey-500"
      />
      <button type="submit" className="bg-gray-200">
        Click me to submit
      </button>
    </form>
  );
};

export default LoginPage;
