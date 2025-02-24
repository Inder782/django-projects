  import TitleForm from '@/components/ui/titleform';
import React from 'react';

  const  Page = async() => {
    const res=await fetch('http://localhost:3001/api/posts')
    const data= await res.json()
    return (
      <div className='flex flex-col items-center justify-center mt-10'>
        {data.map((item:any) => (
          <div key={item.id} className="p-2 bg-white shadow rounded mb-2">
            {item.id}
            <li>
            {item.title}
            </li>
          </div>
        ))}
       <TitleForm/>
      </div>
    );
  };

  export default Page;
