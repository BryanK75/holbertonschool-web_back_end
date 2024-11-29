/*eslint-disable*/
export default function cleanSet(set, start_string) {
    if (typeof start_string !== 'string' || !start_string.length === 0) {
        return '';
    }
    let result = '';
    for (const item of set) {
        if (item.startsWith(start_string)) {
            result += (result ? '-' : '') + item.slice(start_string.length);
        }
    }
    return result;
    }
