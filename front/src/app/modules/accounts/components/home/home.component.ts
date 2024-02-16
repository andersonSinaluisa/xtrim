import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AccountRepository } from '../../../../core/repositories/account.repository';
import { AccountData } from '../../../../core/models/account.model';
import { ModalComponent } from '../../../../modules/shared/components/modal/modal.component';
import { IClientAuthorizeCallbackData, ICreateOrderRequest, IPayPalConfig } from 'ngx-paypal';
import { ItemsPayment } from 'src/app/core/models/paymen.model';
import { PaymentRepository } from 'src/app/core/repositories/payment.repository';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {

  modal: ModalComponent = new ModalComponent();
  

  user_data:AccountData = {
    accounts:[],
    user:{
      created_at:'',
      deleted_at:'',
      email:'',
      first_name:'',
      id:0,
      last_name:'',
      password:'',
      updated_at:''
    }
  }

  showSuccess = false;

  date = new Date().toLocaleString();

  hour = new Date().toLocaleTimeString();


  total_balance = 0;



  modalTitle = 'Tienes valores pendientes';
  modalContent = '';
  closeButtonLabel = 'Pagar deuda';
  cancelButtonLabel = 'Cancelar';
  items_payment:ItemsPayment[] = [];
  
  public payPalConfig?: IPayPalConfig;


  constructor(private readonly accountrepository: AccountRepository, private route :Router, private readonly paymentRepository: PaymentRepository
    ) { }

  openModal() {
    this.modal.isOpen = true;
  }

  closeModal() {
    this.modal.isOpen = false;
  }

  ngOnInit(){
    this.accountrepository.get_by_id().subscribe(
      (data) => {
        this.user_data = data;
        data.accounts.forEach((element) => {
          this.total_balance += parseFloat(element.balance);
          
          this.items_payment.push(new ItemsPayment(element.state+","+element.city+","+element.address,1,
          'DIGITAL_GOODS',parseFloat(element.balance),'USD',
          element.id.toString()
          ));
        })
        if (this.total_balance){
          //redondear a 2 decimales
          this.total_balance = Math.round(this.total_balance * 100) / 100;
          this.modalContent = `Tienes una deuda en tu cuenta de $ ${this.total_balance}`;
          this.openModal();
          this.payConfig(this.items_payment,this.total_balance);

        }
      },
      (error) => {
        //si es 401 redirigir a login
        console.log(error);
        if (error.status === 401) {
          localStorage.removeItem('token');
          this.route.navigate(['/login']);
        }
      }
    )

    
  }




  async calculate_balance(data: { account_id: string; amount: string; }[]) {
    const isSucced = await this.accountrepository.calculate_balance(data)
    if (isSucced) {
      this.showSuccess = true;
      this.closeModal();
      this.accountrepository.get_by_id().subscribe(
        (data) => {
          this.user_data = data;
          
        },
        (error) => {
          //si es 401 redirigir a login
          if (error.status === 401) {
            localStorage.removeItem('token');
            this.route.navigate(['/login']);
          }
        }
      )
    }
  }

   onAction(type:string,message:string,data:IClientAuthorizeCallbackData|null): void {
    

    console.log(type,message);
  }

  private payConfig(items_payment:ItemsPayment[],total_balance:number): void {
    this.payPalConfig = this.paymentRepository.pay(items_payment,total_balance,this.onAction)

    this.payPalConfig.onClientAuthorization = (data) => {
      const order_items:{
        account_id:string,
        amount:string
      }[] = []
      data?.purchase_units[0].items.forEach((element:any) => {
        order_items.push({
          account_id:element.sku,
          amount:element.unit_amount.value
        })
      })
      this.calculate_balance(order_items);
    }
  }


  onLogout() {
    localStorage.removeItem('token');
    this.route.navigate(['/login']);
  }
}
