import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './modules/accounts/components/home/home.component';
import { LoginComponent } from './modules/accounts/components/login/login.component';
import { AuthGuard } from './infrastructure/services/auth.guard';

const routes: Routes = [
  {
    path:'login',
    component: LoginComponent,
    canActivate: [AuthGuard]
  },
  {
    path:'home',
    component: HomeComponent,
  },
  {
    path:'',
    redirectTo:'login',
    pathMatch:'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
