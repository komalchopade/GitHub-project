function validateEmail(email_id) {
    const pattern = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    
    if (pattern.test(email_id)) {
        console.log('The email address is valid');
    }
    else {
        console.log('The email address is not valid');
    }
}

validateEmail('komalganesh24@gmail.com');
validateEmail('hello@com');

