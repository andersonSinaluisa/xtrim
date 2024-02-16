import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AccountRepository } from '../../../../core/repositories/account.repository';
import { AuthModel } from 'src/app/core/models/auth.model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {


  email: string = '';
  password:string = '';

  error:string ='';


  constructor(private readonly accountrepository: AccountRepository, private route :Router) { }




  onEmailChange(event: Event){
    this.email = (event.target as HTMLInputElement).value;
  }

  onPasswordChange(event: Event){
    this.password = (event.target as HTMLInputElement).value;
  }

  onSubmit(event: Event){
    event.preventDefault();
    this.login();
  }


  redirect(data:AuthModel){
    localStorage.setItem('token', data.access_token);

    this.route.navigate(['/home']);
  }


  login(){
    this.accountrepository.login(
      this.email,
      this.password
    ).subscribe(
      (data) => this.redirect(data),
      (error) => {
        console.log(error);
        const message = error.error?.error
        this.error = message || 'An error occurred';
      }    
    )
  }
}
