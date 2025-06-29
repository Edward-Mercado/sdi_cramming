function print(text) {
    console.log(text);
}

function randint(low, high) {
    range = high - low + 1;
    let x = Math.floor(Math.random() * range);
    x += low;
    return x;
}

print("Hello World!");
print(randint(1, 34));