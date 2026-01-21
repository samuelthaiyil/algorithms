function encode(arr: string[]): string {
    let result = "";

    for (const str of arr) {
        result += `${str}  `;
    }

    return result.substring(0, result.length - 2);
}

function decode(arr: string): string[] {
    return arr.split("  ");
}


console.log(decode(encode(["neet","code","love","you"])));