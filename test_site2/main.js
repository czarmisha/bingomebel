var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form ...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    // ... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "Submit";
    } else {
        document.getElementById("nextBtn").innerHTML = "Next";
    }
    // ... and run a function that displays the correct step indicator:
    fixStepIndicator(n)
}

function nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form... :
    if (currentTab >= x.length) {
        //...the form gets submitted:
        document.getElementById("regForm").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function validateForm() {
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[currentTab].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
        // If a field is empty...
        if (y[i].value == "") {
        // add an "invalid" class to the field:
        y[i].className += " invalid";
        // and set the current valid status to false:
        valid = false;
        }
    }
    // If the valid status is true, mark the step as finished and valid:
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid; // return the valid status
}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class to the current step:
    x[n].className += " active";
}

document.querySelector('.close-button').addEventListener('click', function () {
    document.getElementById('multiForm').classList.remove('active');
})


$('.gallery_slider').slick({
    autoplay: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: true,
    arrows: true,
    fade: true,
    appendArrows: $(".gallery_slider_arrows"),
    appendDots: $(".gallery_slider_dots"),
    lazyLoad: 'ondemand',
    prevArrow: '<button type="button" class="slider-prev slider-arrow"></button>',
    nextArrow: '<button type="button" class="slider-next slider-arrow"></button>',
    responsive: [
      {
        breakpoint: 699,
        settings: {
          slidesToShow: 1,
        }
      },
    ]
  });


// Находим все картинки на странице
var $images = $('.gallery_slide img');

// Назначаем обработчик клика на каждую картинку
$images.on('click', function() {
  var $this = $(this);

  // Находим блок, в котором находится картинка
  var $block = $this.closest('.gallery_slide_photo');

  // Находим все картинки в блоке
  var $blockImages = $block.find('img');

  // Создаем элементы слайдера
  var $slider = $('<div class="slider"></div>');

  // Добавляем каждую картинку в слайдер
  $blockImages.each(function() {
    var $slide = $('<div class="slide"></div>');
    var $image = $('<img>');

    $image.attr('src', $(this).attr('src'));

    $slide.append($image);
    $slider.append($slide);
  });

  // Вставляем слайдер в модальное окно
  $('#modal').append($slider);
  
  var $sliderDots = $('<div class="slider_dots"></div>');
  $('#modal').append($sliderDots);

  // Открываем модальное окно
  $('#modal').show();

  // Инициализируем слайдер
  $slider.slick({
    autoplay: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: true,
    arrows: true,
    fade: true,
    appendArrows: $("#modal .slider_arrows"),
    appendDots: $("#modal .slider_dots"),
    lazyLoad: 'ondemand',
    prevArrow: '<button type="button" class="slider-prev slider-arrow"></button>',
    nextArrow: '<button type="button" class="slider-next slider-arrow"></button>',
    responsive: [
      {
        breakpoint: 699,
        settings: {
          slidesToShow: 1,
        }
      },
    ]
  });

  // Назначаем обработчик клика на кнопку закрытия модального окна
  $('#close-modal').on('click', function() {
    // Удаляем слайдер
    $slider.slick('unslick');
    // Удаляем модальное окно
    $('#modal').hide();
    // Отписываемся от обработчика клика на кнопке закрытия модального окна
    $(this).off('click');

    $slider.remove()
    $sliderDots.remove()
  });
});


