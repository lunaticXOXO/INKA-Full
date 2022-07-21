export default class Login {
  constructor() {
    this.KEY = "Login";
  }

  getCurrentUserType() {
    return JSON.parse(localStorage.getItem(this.KEY)) || 'Guest';
  }

  addToUserType(userType) {
    const currentUserType = JSON.parse(localStorage.getItem(this.KEY)) || [];
    currentUserType.push(userType);
    localStorage.setItem(this.KEY, JSON.stringify(currentUserType[0]));
  }

  removeUserType() {
    localStorage.removeItem(this.KEY)
  }
}