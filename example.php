<?php
namespace Drupal\example\Form;
//use Drupal\Core\Form\FormBase;
use Drupal\Core\Form\FormStateInterface;
use Drupal\user\Form\UserPasswordForm;
use Drupal\Core\Url;
use Symfony\Component\HttpFoundation\RedirectResponse;
class ExampleForm extends UserPasswordForm{
    
    public function getFormId()
    {
        return "reset_form_password_page";
    }    

     public function buildForm(array $form, FormStateInterface $form_state)
     {

       $form['passwordconfirm'] = [
           "#type"=>"password_confirm"
       ];
       
       return $form;
    }
    public function validateForm(array &$form, FormStateInterface $form_state)
    {
        //\Drupal::messenger()->addMessage("from validate form");
                $str = $form_state->getTriggeringElement();
            //$this->redirect('<front>');
            \Drupal::messenger()->addMessage("form validateform");
           

               /** $email = $form_state->getValue('email'); 
                if(str_contains($email,"'")){
        
                    $form_state->setErrorByName($email,"legislation.gov.uk Publishing cannot acceptemail address");
                }
                elseif(!\Drupal::service('email.validator')->isValid($email)){
                    $form_state->setErrorByName($email,"not valid email");
                }**/
        
           
            
    }
    public function backToHomeSubmit(){
        \Drupal::messenger()->addMessage("from back to home submit");
        /**$url = Url::fromUri("<front>");
      $path = $url->toString();
      $response = new RedirectResponse($path);
      $response->send();*/
      $url = Url::fromRoute('<front>');
 $response = new RedirectResponse($url->toString());
 $response->send();

    }
    public function submitForm(array &$form, FormStateInterface $form_state)
    {
      \Drupal::messenger()->addMessage("rebuild suceess");
      //$form_state->setRebuild();

            
        
    }
    //public function cancelbutton(&$form ,$form_state){
      //  $this->redirect('<front>');
    //}
    
    
    
}
