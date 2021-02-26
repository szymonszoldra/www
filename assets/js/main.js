const hamburgerBtn = document.querySelector('.hamburger');
const navbarLinks = document.querySelector('.navbar__links');

// Toggle the hamburger button and the navbar links on click
hamburgerBtn.addEventListener('click', (e) => {
  hamburgerBtn.classList.toggle('is-active');
  navbarLinks.classList.toggle('is-active');
});


// Mail handling
const contactForm = document.querySelector('#contact-form');

function handleResultMessage(hasSucceeded) {
  document.querySelectorAll('.form-result').forEach(p => p.style.display = 'none');

  if (hasSucceeded) {
    document.querySelector('.footer-contact__form-positive').style.display = 'block';
  } else {
    document.querySelector('.footer-contact__form-negative').style.display = 'block';
  }
}

global.captchaSubmit = async function (token) {
  const URL = '/contact_form/';
  const data = new URLSearchParams(new FormData(contactForm));
  const headers = new Headers();
  headers.append('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');

  const response = await fetch(URL, {
    method: 'POST',
    body: data,
    headers: headers,
  });

  if (response.status === 200) {
    contactForm.reset();
    handleResultMessage(true);
  } else {
    handleResultMessage(false);
  }
}

global.doCaptcha = function() {
  grecaptcha.reset();
  grecaptcha.execute();
}

function submitContactForm(e) {
  e.preventDefault();

  if (window.captcha !== undefined) {
    doCaptcha();
    return;
  }
  window.captcha = true;

  const script = document.createElement('script');
  document.body.appendChild(script);
  script.src = 'https://www.google.com/recaptcha/api.js?onload=doCaptcha';
}

contactForm.addEventListener('submit', submitContactForm);
document.getElementById('contact-form-button').type = 'submit';
