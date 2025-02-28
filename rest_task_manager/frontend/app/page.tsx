import  { ProfileForm } from "@/components/ui/ProfileForm";

interface Post{
  id:number,
  title:string
}

const Page = async () => {
  try {
    const res = await fetch('http://localhost:3000/api/posts');
    const data = await res.json();

    return (
      <div className="flex flex-col items-center justify-center mt-10">
        <div>
        {data.map((item: Post) => (
          <div key={item.id} className="p-2 bg-white shadow rounded mb-2">
            {item.id}
            <li>{item.title}</li>
          </div>
        ))}
        </div>
        <div>
          <ProfileForm/>
        </div>
      </div>
    );
  } catch (err) {
    console.log(err)
    return <div>Error fetching data.</div>;
  }
};

export default Page;
