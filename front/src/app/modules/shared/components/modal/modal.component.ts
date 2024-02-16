import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-modal',
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.css']
})
export class ModalComponent {

  isOpen = false;
  @Input()
  modalTitle: string = 'Alerta';
  @Input()
  modalContent: string = 'Tienes un saldo en tu cuenta';
  @Input()
  closeButtonLabel: string = 'Cerrar';

  @Input()
  cancelButtonLabel: string = 'Cancelar';

  
  @Output() closeModalEvent = new EventEmitter<void>();

  onCloseModal() {
    this.closeModalEvent.emit();
  }
}
