//Login / Sign_up Start
const wrapper = document.querySelector('.wrapper');
const loginlink = document.querySelector('.login-link');
const registerlink = document.querySelector('.register-link');

registerlink.addEventListener('click', ()=>{
    wrapper.classList.add('active')
})

loginlink.addEventListener('click', ()=>{
    wrapper.classList.remove('active')
})

//Login / Sign_up End

//reset password
const wrapper2 = document.querySelector('.wrapper');
const loginlink3 = document.querySelector('.login-link');
const resetpassword =document.querySelector('.reset-link')

resetpassword.addEventListener('click', ()=>{
    wrapper2.classList.add('active2')
})

loginlink3.addEventListener('click', ()=>{
    wrapper2.classList.remove('active2')
})