import { Injectable } from '@angular/core';
import { DropdownQuestion } from './question-dropdown';
import { QuestionBase } from './question-base';
import { TextboxQuestion } from './question-textbox';
import { of } from 'rxjs';

@Injectable()
export class QuestionService {

  // TODO: get from a remote source of question metadata
  getQuestions() {

    const questions: QuestionBase<string>[] = [

      new DropdownQuestion({
        key: 'strength',
        label: 'escala de força',
        options: [
          {key: 'bodybuilder', value: 'fisiculturista'},
          {key: 'forte', value: 'forte'},
          {key: 'fraco', value: 'fraco'},
          {key: 'frangolino', value: 'frango'}
        ],
        order: 3
      }),

      new TextboxQuestion({
        key: 'firstName',
        label: 'Nome Completo',
        value: 'stefano',
        required: true,
        order: 1
      }),

      new TextboxQuestion({
        key: 'Telefone',
        label: 'telefone',
        type: 'cellphone',
        order: 2
      }),
    

      new TextboxQuestion({
        key: 'emailAddress',
        label: 'Email',
        type: 'email',
        order: 3
      })
    ];

      


    return of(questions.sort((a, b) => a.order - b.order));
  }
}