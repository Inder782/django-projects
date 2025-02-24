import { NextResponse } from "next/server";

export async function GET(){
    const data=await fetch("http://127.0.0.1:8000/all")
    const res = await data.json()
    
    return NextResponse.json(res,{status:200})
}

export async function POST(){
    console.log("you reached me ")
    return NextResponse.json({message:"You reacher here"})
}