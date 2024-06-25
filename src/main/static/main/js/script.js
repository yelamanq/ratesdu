function setRating() {
	var div_list = document.querySelectorAll('.stars-foreground');
	var div_array = [...div_list];
	div_array.forEach(div => {
		const starsTotal = 5;
	    const starPercentageRounded = `${(div.dataset.rating / starsTotal) * 100}%`;
	    div.style.width = starPercentageRounded;

	});

}

function editPasswordType() {
	eye = document.getElementById('eye')
	password = document.getElementById('id_password')
	if (password.type == 'password') {
		password.type = 'text'
		eye.src = eye.getAttribute('data-close')
	} else {
		password.type = 'password'
		eye.src = eye.getAttribute('data-open')
	}
}

function wrong() {
	const elements = document.querySelectorAll('.shake');
	elements.forEach(element => {
	    if (element.classList.contains('shake')) {
	        element.classList.add('wrong');
	        setTimeout(() => {
	            element.classList.remove('wrong');
	        }, 500);
	    }
	});
}


navProfiles = document.querySelector('.nav_profiles')
			menuDropdown = document.querySelector('.menu_dropdown')
			navProfileBurger = document.querySelector('.nav_profile_burger')

			navProfiles.addEventListener('click', () => {
				menuDropdown.classList.toggle('dropdown_active')
				navProfileBurger.classList.toggle('active')
			})









