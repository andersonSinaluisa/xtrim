
import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AccountService } from './account.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private accountService: AccountService, private router: Router) {}

  canActivate(): boolean {
    if (this.accountService.isLogged()) {
      // El usuario está autenticado, redirige a la página principal o a la página que prefieras
      this.router.navigate(['/home']);
      return false;
    }
    return true;
  }
}