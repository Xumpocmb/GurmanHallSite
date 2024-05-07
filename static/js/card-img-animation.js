document.querySelectorAll(".big-card__card-block").forEach(function (card) {
  card.addEventListener("mousemove", function (e) {
    let rect = card.getBoundingClientRect();
    let x = e.clientX - rect.left;
    let y = e.clientY - rect.top;
    card.querySelector(
      ".big-card__img"
    ).style.transformOrigin = `${x}px ${y}px`;
  });
});

    var docWidth = document.documentElement.offsetWidth;
    [].forEach.call(document.querySelectorAll("*"), function (el) {
      if (el.offsetWidth > docWidth) {
        console.log(el);
      }
    });