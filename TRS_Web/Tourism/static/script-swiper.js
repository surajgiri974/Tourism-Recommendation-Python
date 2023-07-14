var swiper = new Swiper('.review-slider', {
   spaceBetween: 20,
   loop: true,
   autoplay: {
      delay: 2500,
      disableOnInteraction: false,
   },
   breakpoints: {
      640: {
         slidesPerView: 1,
      },
      768: {
         slidesPerView: 2,
      },
      1024: {
         slidesPerView: 3,
      },
   }
});

var swiper = new Swiper('.brand-slider', {
   spaceBetween: 20,
   loop: true,
   autoplay: {
      delay: 2500,
      disableOnInteraction: false,
   },
   breakpoints: {
      640: {
         slidesPerView: 2,
      },
      768: {
         slidesPerView: 3,
      },
      991: {
         slidesPerView: 4,
      },
      1200: {
         slidesPerView: 5,
      },
   }
});