const bigCardRadioButtons = document.querySelectorAll('.big-card__item-size-radio');
const bigCardSelectAddons = document.querySelectorAll('.big-card__checkbox');
const bigCardSelectBoard = document.querySelector('.show-modal__select');
const priceElement = document.querySelector(`.show-modal__basket-title-price`);


bigCardRadioButtons.forEach((button) => {
    button.addEventListener('change', (event) => {
        let URL = '/catalog/get_item_params_price/';
        let paramID = event.target.value;
        URL += '?param_id=' + paramID;
        console.log(URL);

        // Определяем, выбран ли борт
        let selectedBoard = bigCardSelectBoard.value;
        let sizeID;
        if (selectedBoard !== '0') {
            // Если выбран, надо узнать размер пиццы
            sizeID = event.target.id.split('-')[3];
            URL += '&board_id=' + selectedBoard + '&size_id=' + sizeID;
        } else {
            sizeID = '0'
        }

        let selectedAddons = [];
        bigCardSelectAddons.forEach(addon => {
            if (addon.checked) {
                selectedAddons.push(addon.value);
            }
        });
        URL += '&addons=' + selectedAddons.join(',');

        // Отправляем AJAX-запрос для получения информации
        fetch(URL)
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // Обновляем цену на странице
                priceElement.textContent = data.final_price + ' р.';
            })
            .catch(function (error) {
                // Обработка ошибки
                console.log(error);
            });
    });
});

bigCardSelectBoard.addEventListener('change', (event) => {
    console.log(event.target.value);
    let URL = '/catalog/get_item_params_price/';
    let selectedBoard = event.target.value;
    URL += '?board_id=' + selectedBoard;

    // Узнаем выбранный размер
    bigCardRadioButtons.forEach((button) => {
        if (button.checked) {
            let paramID = button.value;
            let sizeID = button.id.split('-')[3];
            URL += '&param_id=' + paramID + '&size_id=' + sizeID;
        }
    })

    let selectedAddons = [];
        bigCardSelectAddons.forEach(addon => {
            if (addon.checked) {
                selectedAddons.push(addon.value);
            }
        });
        URL += '&addons=' + selectedAddons.join(',');

    fetch(URL)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // Обновляем цену на странице
            priceElement.textContent = data.final_price + ' р.';
        })
        .catch(function (error) {
            // Обработка ошибки
            console.log(error);
        });
});


bigCardSelectAddons.forEach((addon) => {
    addon.addEventListener('change', (event) => {

        // Собираем информацию о выбранных добавках
        let selectedAddons = [];
        bigCardSelectAddons.forEach(addon => {
            if (addon.checked) {
                selectedAddons.push(addon.value);
            }
        });
        let URL = '/catalog/get_item_params_price/';
        URL += '?addons=' + selectedAddons.join(',');

        // Узнаем выбранный размер
        bigCardRadioButtons.forEach((button) => {
            if (button.checked) {
                let paramID = button.value;
                let sizeID = button.id.split('-')[3];
                URL += '&param_id=' + paramID + '&size_id=' + sizeID;
            }
        })

        // Определяем, выбран ли борт
        let selectedBoard = bigCardSelectBoard.value;
        let sizeID;
        if (selectedBoard !== '0') {
            // Если выбран, надо узнать размер пиццы
            sizeID = event.target.id.split('-')[3];
            URL += '&board_id=' + selectedBoard;
            console.log(URL);
        } else {
            sizeID = '0'
        }


        fetch(URL)
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // Обновляем цену на странице
                priceElement.textContent = data.final_price + ' р.';
            })
            .catch(function (error) {
                // Обработка ошибки
                console.log(error);
            });
    });
})