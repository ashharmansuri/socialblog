console.log('i am custom validation')
const usernameInput = document.querySelector('#usernameInput');
const feedBack = document.querySelector('.invalid-feedback');
usernameInput.addEventListener('keyup', (e)=>{
//   console.log("77",777)
  
  const usernameVal = e.target.value;
  console.log('usernameVal',usernameVal);
  
  usernameInput.classList.remove('is-invalid');
  feedBack.style.display ='none';
  


   // api clearInterval
   if(usernameVal.length>0){
   fetch("/validate-username",{
       body:JSON.stringify({username : usernameVal}),
       method:"POST",

   
     })
     .then(res=>res.json())
     .then(data=>{
         if(data.username_error){
             usernameInput.classList.add('is-invalid');
             feedBack.style.display ='block';
             feedBack.innerHTML=`<p> ${data.username_error} </p>`;
         }
     });
   }
});