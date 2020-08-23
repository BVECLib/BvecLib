class AnimatedNavbar {
    constructor(navId, buttonId) {
        this.navbar = document.getElementById(navId);
        this.button = document.getElementById(buttonId);
        this.status = 'closed';
        this.init();
    }
    init() {
        this.button.addEventListener('click', () => { this.work(); });
    }
    work() {
        if (this.status == 'closed') {
            this.open();
            this.changeButtonToClose();
        } else {
            this.close();
            this.changeButtonToOpen();
        }
    }
    open() {
        this.navbar.style.width = '100%';
        this.status = 'open';
    }
    close() {
        this.navbar.style.width = '0%';
        this.status = 'closed';
    }
    changeButtonToOpen() {
        this.button.innerHTML = '<i class="fas fa-bars"></i>';
    }
    changeButtonToClose() {
        this.button.innerHTML = '<i class="fas fa-times"></i>';
    }

}

let nav = new AnimatedNavbar('myNav', 'openNav');