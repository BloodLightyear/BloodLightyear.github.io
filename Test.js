// forms.js
//


const init = function(){
    document.getElementById('button-reset').addEventListener('click', reset);
    document.getElementById('button-submit').addEventListener('click', send);
}

const reset = function(ev){
    //HTML will automatically put the form back to its initial state
    //unless we do 
    ev.preventDefault();
    // programmatically we can reset it 
    document.getElementById('form-user').reset();
    //if you want to do anything else...
}

const send = function(ev){
    ev.preventDefault(); 
    ev.stopPropagation();
    //or the click will travel to the form and the form will submit
    let fails = validate();
    //IF we wanted to do some async things then use a Promise with .then and .catch
    if(fails.length === 0){
        //good to go
        document.getElementById('form-user').submit();
    }else{
        //there are some errors to display
        //bad user
        //let err = document.querySelector('.error');
        //let input = err.querySelector('input');
        //err.setAttribute('data-errormsg', ` ... Missing ${input.placeholder}`);
        fails.forEach(function(obj){
            let field = document.getElementById(obj.input);
            field.parentElement.classList.add('error');
            field.parentElement.setAttribute('data-errormsg', obj.msg);
        })
    }
}

const validate = function(ev){
    //let valid = true;
    let failures = [];
    //checkbox (or radio buttons grouped by name)
    let chk = document.getElementById('LOW01');
    // .checked .value
    if(chk.checked){
        //valid = false;
        //chk.parentElement.classList.add('error');
        //chk.parentElement.setAttribute('data-errormsg', 'Must be alive to submit.');
        failures.push({input: 'LOW01', msg: ' CMQCC Stratification: Low '})
    }
    //return a boolean || an object with details about the failures
    return failures;
}


document.addEventListener('DOMContentLoaded', init);
