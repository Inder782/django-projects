import { NextResponse } from "next/server";

export async function GET(){
    try{
        const data=await fetch("http://127.0.0.1:8000/all")
        const res = await data.json()

        return NextResponse.json(res,{status:200})
    }
    catch(err){
        console.log(err)
        return NextResponse.json({"message":"something went wrong"},{status:500})
    }

    
}

export async function POST(request:Request){
    const data = await request.json()

    const req= await fetch("http://127.0.0.1:8000/create",
    {method:"POST",
    headers: { "Content-Type": "application/json" },
    body:JSON.stringify(data)
    })
    const resp= await req.json()
    console.log(resp)
    return NextResponse.json({message:"You reacher here"})
}