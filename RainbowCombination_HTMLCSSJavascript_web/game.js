const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// 定义颜色和等级
const rainbowColors = ['#FF6961', '#FFB347', '#ffe338', '#8BC68B', '#6fd9cf', '#4c78ae', '#9f8cc3'];
const colorLevel = {
    '#FF6961': 1, '#FFB347': 2, '#ffe338': 3,
    '#8BC68B': 4, '#6fd9cf': 5, '#4c78ae': 6, '#9f8cc3': 7
};

let sticks = [];
let liftedBalls = []; // 被提起的小球
let incomingBalls = [];
let moveCount = 0;
let gameOver = false;
let score = 0;
let clicksLeft = 8;
let countdown = 5;

// 控制面板元素
const startButton = document.getElementById('startButton');
const restartButton = document.getElementById('restartButton');
const scoreLabel = document.getElementById('scoreLabel');
const clicksLeftLabel = document.getElementById('clicksLeftLabel');
const countdownLabel = document.getElementById('countdownLabel');

// 信息显示容器
const startMessage = document.getElementById('startMessage');

// Stick类
class Stick {
    constructor(x, balls = []) {
        this.x = x;
        this.balls = balls;
    }

    addBall(ball) {
        this.balls.push(ball);
    }

    removeTopBall() {
        return this.balls.pop();
    }

    getTopBall() {
        return this.balls.length ? this.balls[this.balls.length - 1] : null;
    }

    getSecondTopBall() {
        return this.balls.length > 1 ? this.balls[this.balls.length - 2] : null;
    }

    isFull() {
        return this.balls.length >= 7;
    }
}

// 创建球并在上面绘制等级数字
function createBall(x, y, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, 40, 0, Math.PI * 2);
    ctx.fill();
    ctx.closePath();

    // 绘制数字，代表等级
    const level = colorLevel[color];
    if (level) { // 确保等级存在
        ctx.fillStyle = 'black';
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(level, x, y);
    }
}

// 初始化游戏
function initializeGame() {
    gameOver = false;
    score = 0;
    sticks = [];
    liftedBalls = [];
    incomingBalls = [];
    moveCount = 0;
    clicksLeft = 8;

    updateScoreLabel();
    updateClicksLeftLabel();

    // 创建 6 个 Stick，每个 Stick 初始化两个 Level 1 的球
    for (let i = 0; i < 6; i++) {
        sticks.push(new Stick(100 + i * 120, [
            { color: rainbowColors[0], x: 100 + i * 120, y: 750 },
            { color: rainbowColors[0], x: 100 + i * 120, y: 670 }
        ]));
    }

    drawSticks();
}

// 绘制所有 Stick 和上面的球
function drawSticks() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // 清空画布

    sticks.forEach(stick => {
        // 绘制 Stick
        ctx.strokeStyle = 'tan';
        ctx.lineWidth = 10;
        ctx.beginPath();
        ctx.moveTo(stick.x, 200);
        ctx.lineTo(stick.x, 800);
        ctx.stroke();

        // 绘制每个球，并确保从 Stick 底部开始堆叠
        const baseY = 750; // Stick 底部的 Y 坐标
        const ballSpacing = 80; // 球之间的间距（固定的）

        stick.balls.forEach((ball, index) => {
            const ballY = baseY - index * ballSpacing; // 计算每个球的 Y 坐标，从底部往上排列
            createBall(stick.x, ballY, ball.color);
            ball.y = ballY; // 更新球的 Y 坐标
        });
    });
}

function updateScoreLabel() {
    scoreLabel.textContent = `Score: ${score}`;
}

function updateClicksLeftLabel() {
    clicksLeftLabel.textContent = `Clicks left: ${clicksLeft}`;
}

// 处理球的提升和放下
canvas.addEventListener('click', (event) => {
    if (gameOver) return;

    const x = event.offsetX;
    let selectedStick = null;

    // 检测哪个 Stick 被点击了
    sticks.forEach((stick, index) => {
        if (Math.abs(x - stick.x) < 40) { // 如果点击在 Stick 附近
            selectedStick = index;
        }
    });

    if (selectedStick !== null) {
        // 如果已经提起了球，则放下到选中的 Stick 上
        if (liftedBalls.length > 0) {
            dropBalls(selectedStick);
        } else { // 否则提起球
            liftBalls(selectedStick);
        }

        moveCount++;
        if (moveCount === 8) {
            moveCount = 0;
            showNextBalls();
            setTimeout(dropNewBalls, 5000);
        }

        clicksLeft--;
        updateClicksLeftLabel();
    }
});

// 提升球，若两个颜色相同的球在顶部，提升两个球
function liftBalls(stickIndex) {
    let stick = sticks[stickIndex];
    if (stick.balls.length > 0) {
        let topBall = stick.getTopBall();
        let secondTopBall = stick.getSecondTopBall();
        
        if (secondTopBall && topBall.color === secondTopBall.color) {
            liftedBalls.push(secondTopBall);  // 提升第二个球
            liftedBalls.push(topBall);        // 提升第一个球
            stick.balls.pop();                // 移除顶部两个球
            stick.balls.pop();
        } else {
            liftedBalls.push(topBall);        // 只提升顶部的球
            stick.removeTopBall();
        }

        liftedBalls.forEach(ball => ball.y -= 100); // 提升球的 y 坐标
        drawSticks(); // 重新绘制
    }
}

// 放下球
function dropBalls(stickIndex) {
    let stick = sticks[stickIndex];
    if (!stick.isFull()) {
        liftedBalls.forEach(liftedBall => {
            // 从 Stick 底部开始堆叠，计算正确的 Y 坐标
            liftedBall.y = 750 - stick.balls.length * 80;
            stick.addBall(liftedBall); // 添加球到 Stick
        });
        liftedBalls = []; // 清空提起的球

        mergeBalls(stick); // 检查是否可以合并
        drawSticks(); // 重新绘制
    }
}

// 根据相同等级的3或4个球合并
function mergeBalls(stick) {
    let mergeStartIndex = null;
    let mergeLength = 0;

    // 检查从底部到顶部的相邻球
    for (let i = 0; i < stick.balls.length - 2; i++) {
        const color = stick.balls[i].color;
        
        // 找到连续相同颜色的球
        mergeLength = 1; // 至少有一个球
        for (let j = i + 1; j < stick.balls.length && stick.balls[j].color === color; j++) {
            mergeLength++;
        }

        // 如果找到了3个或4个相同颜色的球
        if (mergeLength >= 3) {
            mergeStartIndex = i;
            break;
        }
    }

    // 如果找到了符合条件的合并区域
    if (mergeStartIndex !== null && mergeLength >= 3) {
        let color = stick.balls[mergeStartIndex].color;
        let newLevelColor = rainbowColors[(colorLevel[color]) % rainbowColors.length]; // 修复新颜色生成

        // 移除这段区域的球
        stick.balls.splice(mergeStartIndex, mergeLength);

        // 添加一个新的高一级的球
        stick.balls.push({ color: newLevelColor, x: stick.x, y: 750 - stick.balls.length * 80 });

        // 如果是最高等级，增加分数
        if (newLevelColor === rainbowColors[6]) {
            score += 20;
        }

        updateScoreLabel();
    }
}

// 显示下一个要掉落的球
function showNextBalls() {
    countdownLabel.textContent = `Time left: 5`;
    let interval = setInterval(() => {
        countdown--;
        countdownLabel.textContent = `Time left: ${countdown}`;
        if (countdown === 0) {
            clearInterval(interval);
            countdown = 5;
        }
    }, 1000);
}

// 掉落新球到每个 Stick
function dropNewBalls() {
    sticks.forEach(stick => {
        if (!stick.isFull()) {
            let newBallColor = rainbowColors[Math.floor(Math.random() * getHighestLevel())];
            stick.addBall({ color: newBallColor, x: stick.x, y: 750 - stick.balls.length * 80 });

            // 检查是否符合合并条件（顶部两个球和新球颜色相同）
            if (stick.balls.length >= 3) {
                const topBall = stick.getTopBall();
                const secondBall = stick.getSecondTopBall();
                
                // 如果新球与最上方两个球颜色相同，触发合并
                if (topBall.color === secondBall.color && newBallColor === topBall.color) {
                    mergeBalls(stick);
                }
            }
        }
    });
    drawSticks();
}

// 获取最高等级
function getHighestLevel() {
    return Math.max(...sticks.flatMap(stick => stick.balls.map(ball => colorLevel[ball.color])));
}

// 开始和重启按钮
startButton.addEventListener('click', () => {
    startMessage.style.display = 'none'; // 隐藏开始信息
    initializeGame();
    startButton.style.display = 'none';
    restartButton.style.display = 'block';
});

restartButton.addEventListener('click', () => {
    initializeGame();
});

// 页面加载时初始化游戏
initializeGame();
