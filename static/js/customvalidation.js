console.log('i am custom validation')
const usernameInput = document.querySelector('#usernameInput');
const usernamefeedBack = document.querySelector('.usernamefeedback');
const emailfeedBack = document.querySelector('.emailfeedback');
const emailInput = document.querySelector('#emailInput');
const usernamesuccess = document.querySelector('.username-success-output');

emailInput.addEventListener('keyup',(e)=>{
       const emailVal = e.target.value;
       console.log('emailVal',emailVal);
      
       emailInput.classList.remove('is-invalid');
       emailfeedBack.style.display ='none';
      

       // api clearInterval
   if(emailVal.length>0){
    fetch("/validate-email",{
        body:JSON.stringify({email : emailVal}),
        method:"POST",
 
    
      })
      .then(res=>res.json())
      .then(data=>{
          if(data.email_error){
              emailInput.classList.add('is-invalid');
              emailfeedBack.style.display ='block';
              emailfeedBack.innerHTML=`<p> ${data.email_error} </p>`;
          }
      });
    }
});





usernameInput.addEventListener('keyup', (e)=>{
//   console.log("77",777)
  
  const usernameVal = e.target.value;
  console.log('usernameVal',usernameVal);
  // usernamesuccess.style.display='block';
  // usernamesuccess.textContent=`Checking ${usernameVal}`

  usernameInput.classList.remove('is-invalid');
  usernamefeedBack.style.display ='none';
  


   // api clearInterval
   if(usernameVal.length>0){
   fetch("/validate-username",{
       body:JSON.stringify({username : usernameVal}),
       method:"POST",

   
     })
     .then(res=>res.json())
     .then(data=>{
        //  usernamesuccess.style.display='none';
         if(data.username_error){
             usernameInput.classList.add('is-invalid');
             usernamefeedBack.style.display ='block';
             usernamefeedBack.innerHTML=`<p> ${data.username_error} </p>`;
         }
     });
   }
});

