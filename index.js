let rewards = [];

window.addEventListener('load', async function() {
    try {
        const response = await fetch('https://sorbia.pythonanywhere.com/rewards');
        rewards = await response.json(); // ذخیره در متغیر전역

        const rewardsList = document.getElementById('rewardsList');

        rewards.forEach((reward, index) => {
            const newItem = document.createElement('div');
            newItem.className = 'list-item';
            newItem.id = `item${index}`;
    
            newItem.innerHTML = `
                ${reward.icon}
                <div class="item-content">
                    <div class="item-title">${reward.name}</div>
                    <div class="item-reward">${reward.value}</div>
                </div>
                <i class="fas fa-chevron-right arrow-icon"></i>
            `;
    
            rewardsList.appendChild(newItem);
        });
    } catch (error) {
        console.error('خطا در دریافت اطلاعات:', error);
    }
});
    function handleItemClick(itemId, reward) {
        try {
            const rewardIndex = parseInt(itemId.replace('item', ''));
            const customFunction = rewards[rewardIndex].function;
            console.log(customFunction);
            if (customFunction) {
                // اجرای تابع سفارشی
                eval(customFunction);
            } else {
                alert(`پاداش شما به مقدار ${reward} دریافت شد!`);
            }
        } catch (error) {
            console.log(`آیتم ${itemId} کلیک شد - پاداش: ${reward}`);
            alert(`پاداش شما به مقدار ${reward} دریافت شد!`);
        }
    }

document.getElementById('rewardsList').addEventListener('click', function (e) {
    if (e.target.closest('.list-item')) {
        const item = e.target.closest('.list-item');
        const reward = item.querySelector('.item-reward').textContent;
        handleItemClick(item.id, reward);
    }
});
