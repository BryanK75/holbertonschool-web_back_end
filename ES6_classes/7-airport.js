export default class Airport {
    constructor (name, code) {
      if (typeof name !== 'string')
        throw new TypeError ('name must be a string');
      if (typeof code !== 'string')
        throw new TypeError ('code must be a string');
      this._name = name;
      this._code = code;
    }
  
    get name() {
      return this._name;
    }
  
    set name(value) {
      if (typeof value !== 'string')
        throw new TypeError ('name must be a string');
      this._name = value;
    }
  
    get code() {
      return this._code;
    }
  
    set code(value) {
      if (typeof value !== 'string')
        throw new TypeError ('code must be a string');
      this._code = value;
    }
  
    toString() {
      return `[object ${this._code}]`;
    }
  }