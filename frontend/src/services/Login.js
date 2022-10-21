export default class Login {
  constructor() {
    this.KEY = "super secret key";
    this.username = ""
  }

  getCurrentUserType() {
    return JSON.parse(localStorage.getItem(this.KEY)) || 'Guest';
  }

  getCurrentUsername(){
    return JSON.parse(localStorage.getItem(this.username)) || 'Guest';
  }

  addToUserType(userType) {
    const currentUserType = JSON.parse(localStorage.getItem(this.KEY)) || [];
    currentUserType.push(userType);
    localStorage.setItem(this.KEY, JSON.stringify(currentUserType[0]));
  }
  
  addToUsername(username) {
    const currentUsername = JSON.parse(localStorage.getItem(this.username)) || [];
    currentUsername.push(username);
    localStorage.setItem(this.username, JSON.stringify(currentUsername[0]));
  }

  removeUserType() {
    localStorage.removeItem(this.KEY)
    localStorage.clear()
  }
}