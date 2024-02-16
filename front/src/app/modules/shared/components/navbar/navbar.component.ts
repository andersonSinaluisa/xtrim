import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {


  @Input()
  isSession: boolean=false;
  
  @Output() logout = new EventEmitter<void>();

  ngOnInit(): void {
    this.setVisibilityClasses();
  }
  visibilityClasses: {} = {
    'opacity-0': false,
    'opacity-100': false
  
  };
   isVisible: boolean = false;
  toggleVisible(isVisible: boolean): void {
    console.log(`is the menu open: ${isVisible ? 'Yes' : 'No'}`)
    this.isVisible = isVisible;
    this.setVisibilityClasses();
  }
  private setVisibilityClasses(): void {
    this.visibilityClasses = {
      'opacity-0': !this.isVisible,
      'opacity-100': this.isVisible
    };
  }

  onLogout() {
    this.logout.emit();
  }
}
