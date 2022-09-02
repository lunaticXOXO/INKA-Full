export default class Login {
  constructor() {
    this.KEY = "super secret key";
    this.username = ""
  }

  getCurrentUserType() {
    console.log("Get Item: ", JSON.parse(localStorage.getItem(this.KEY)))
    return JSON.parse(localStorage.getItem(this.KEY)) || 'Guest';
  }

  getCurrentUsername(){
    console.log("Get Username: ", JSON.parse(localStorage.getItem(this.username)))
    return JSON.parse(localStorage.getItem(this.username)) || 'Guest';
  }

  addToUserType(userType) {
    const currentUserType = JSON.parse(localStorage.getItem(this.KEY)) || [];
    currentUserType.push(userType);
    console.log("Set Item: ", this.KEY, JSON.stringify(currentUserType[0]))
    localStorage.setItem(this.KEY, JSON.stringify(currentUserType[0]));
  }

  
  addToUsername(username) {
    const currentUsername = JSON.parse(localStorage.getItem(this.username)) || [];
    currentUsername.push(username);
    console.log("Set username: ", this.username, JSON.stringify(currentUsername[0]))
    localStorage.setItem(this.username, JSON.stringify(currentUsername[0]));
  }
  

  removeUserType() {
    localStorage.removeItem(this.KEY)
    localStorage.clear()
  }
}