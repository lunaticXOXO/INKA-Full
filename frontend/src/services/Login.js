export default class Login {
  constructor() {
    this.KEY = "super secret key";
  }

  getCurrentUserType() {
    console.log("Get Item: ", JSON.parse(localStorage.getItem(this.KEY)))
    return JSON.parse(localStorage.getItem(this.KEY)) || 'Guest';
  }

  addToUserType(userType) {
    const currentUserType = JSON.parse(localStorage.getItem(this.KEY)) || [];
    currentUserType.push(userType);
    console.log("Set Item: ", this.KEY, JSON.stringify(currentUserType[0]))
    localStorage.setItem(this.KEY, JSON.stringify(currentUserType[0]));
  }

  removeUserType() {
    localStorage.removeItem(this.KEY)
    localStorage.clear()
  }
}